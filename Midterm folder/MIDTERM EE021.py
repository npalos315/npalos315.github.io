import matplotlib.pyplot as plt
import numpy as np
import scipy.io.wavfile as wav

print("Voice Recognition Analysis Project")
print("This program studies how voice assistants such as Alexa can recognize different speakers.")
print("Users can graph waveforms, analyze frequencies, and compare voice recordings.")

choice = ""

while choice != "4":

    print("\nVoice Analysis Menu")
    print("1 - Graph a Voice Waveform")
    print("2 - Analyze Dominant Frequency")
    print("3 - Compare Two Voice Recordings")
    print("4 - Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        filename = input("Enter WAV file name: ")

        rate, data = wav.read(filename)

        if len(data.shape) > 1:
            data = data[:, 0]

        plt.plot(data)
        plt.title("Waveform of " + filename)
        plt.xlabel("Sample Number")
        plt.ylabel("Amplitude")
        plt.show()

    elif choice == "2":

        filename = input("Enter WAV file name: ")

        rate, data = wav.read(filename)

        if len(data.shape) > 1:
            data = data[:, 0]

        fft_data = np.fft.fft(data)

        frequencies = np.fft.fftfreq(len(data), d=1/rate)

        dominant_frequency = abs(
            frequencies[np.argmax(np.abs(fft_data))]
        )

        print("\nFrequency Analysis Results")
        print("Dominant Frequency:", round(dominant_frequency, 2), "Hz")

        if dominant_frequency < 200:
            print("This voice has a relatively lower pitch.")
        else:
            print("This voice has a relatively higher pitch.")

    elif choice == "3":

        file1 = input("Enter first WAV file: ")
        file2 = input("Enter second WAV file: ")

        rate1, data1 = wav.read(file1)
        rate2, data2 = wav.read(file2)

        if len(data1.shape) > 1:
            data1 = data1[:, 0]

        if len(data2.shape) > 1:
            data2 = data2[:, 0]

        files = [file1, file2]

        print("\nComparing these files:")

        for name in files:
            print(name)

        plt.plot(data1, label=file1)
        plt.plot(data2, label=file2)

        plt.title("Voice Comparison")
        plt.xlabel("Sample Number")
        plt.ylabel("Amplitude")
        plt.legend()
        plt.show()

        print("Different waveform patterns can help voice assistants distinguish speakers.")

    elif choice == "4":

        print("Exiting program. Thank you!")

    else:

        print("Invalid choice. Please enter 1, 2, 3, or 4.")