class MelgramTest(tf.test.TestCase):
  def test_layer(self):

    test_sr = 16000

    # tensorflow
    mel_layer = LogMelgramLayer(
        num_fft=1024,
        hop_length=512,
        num_mels=128,
        sample_rate=test_sr,
        f_min=0.0,
        f_max=test_sr // 2,
        eps=1e-6,
    )

    np.random.seed(123)
    src = np.random.randn(test_sr, ).astype(np.float32)
    tf_logmelgram = mel_layer(src.reshape(1, -1))[0, :, :, 0]  # single item, remove channel axis

    # librosa
    librosa_stft = np.abs(librosa.stft(y=src,
                                       n_fft=1024,
                                       hop_length=512,
                                       center=False,
                                       win_length=1024))
    linear_to_mel = librosa.filters.mel(sr=test_sr,
                                        n_fft=1024,
                                        n_mels=128,
                                        fmin=0,
                                        fmax=test_sr // 2,
                                        htk=True,
                                        norm=None)

    librosa_melgram = np.dot(librosa_stft.T ** 2, linear_to_mel.T).astype(np.float32)
    librosa_logmelgram = np.log10(librosa_melgram + 1e-6)
    # result
    #  – Max absolute difference: 0.00492716
    #  – Max relative difference: 0.10149292
    self.assertEqual(tf_logmelgram.shape, librosa_logmelgram.shape)
    self.assertAllClose(librosa_logmelgram, tf_logmelgram, rtol=1e-3, atol=1e-2)
