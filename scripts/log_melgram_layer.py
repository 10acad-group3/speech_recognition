import tensorflow as tf
from tensorflow.keras.layers import *
from tensorflow.keras.models import Model, Sequential


class LogMelgramLayer(Layer):
  def __init__(self, num_fft, hop_length, num_mels, sample_rate, f_min, f_max, eps, **kwargs):
    super(LogMelgramLayer, self).__init__(**kwargs)

    self.num_fft = num_fft
    self.hop_length = hop_length
    self.num_mels = num_mels
    self.sample_rate = sample_rate
    self.f_min = f_min
    self.f_max = f_max
    self.eps = eps
    self.num_freqs = num_fft // 2 + 1
    lin_to_mel_matrix = tf.signal.linear_to_mel_weight_matrix(
        num_mel_bins=self.num_mels,
        num_spectrogram_bins=self.num_freqs,
        sample_rate=self.sample_rate,
        lower_edge_hertz=self.f_min,
        upper_edge_hertz=self.f_max,
    )

    self.lin_to_mel_matrix = lin_to_mel_matrix

  def build(self, input_shape):
    self.non_trainable_weights.append(self.lin_to_mel_matrix)
    super(LogMelgramLayer, self).build(input_shape)

  def call(self, input):

    def _tf_log10(x):
      numerator = tf.math.log(x)
      denominator = tf.math.log(tf.constant(10, dtype=numerator.dtype))
      return numerator / denominator

    stfts = tf.signal.stft(
        input,
        frame_length=self.num_fft,
        frame_step=self.hop_length,
        pad_end=False,  # librosa test compatibility
    )
    mag_stfts = tf.abs(stfts)

    melgrams = tf.tensordot(  # assuming channel_first, so (b, c, f, t)
        tf.square(mag_stfts), self.lin_to_mel_matrix, axes=[2, 0]
    )
    log_melgrams = _tf_log10(melgrams + self.eps)
    return tf.expand_dims(log_melgrams, 3)

  def get_config(self):
    config = {
        'num_fft': self.num_fft,
        'hop_length': self.hop_length,
        'num_mels': self.num_mels,
        'sample_rate': self.sample_rate,
        'f_min': self.f_min,
        'f_max': self.f_max,
        'eps': self.eps,
    }
    base_config = super(LogMelgramLayer, self).get_config()
    return dict(list(config.items()) + list(base_config.items()))
