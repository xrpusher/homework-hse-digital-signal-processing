from scipy.fft import fft, fftfreq

SAMPLE_RATE = 10000  # Гц
DURATION = 3  # Секунды

def generate_sin_wave(freq, sample_rate, duration):
    x = np.linspace(0, duration, sample_rate*duration, endpoint=False)
    frequencies = x * freq
    # 2pi для преобразования в радианы
    y = np.sin((2 * np.pi) * frequencies)
    return x, y

# 1 задание
# Генерируем переодический сигнал с частотой 4 Гц, на конечном интервале времени 3 секунды
x, y = generate_sin_wave(4, SAMPLE_RATE, DURATION)


_, nice_tone = generate_sin_wave(400, SAMPLE_RATE, DURATION)
_, noise_tone = generate_sin_wave(4000, SAMPLE_RATE, DURATION)
noise_tone = noise_tone * 0.3

mixed_tone = nice_tone + noise_tone

normalized_tone = np.int16((mixed_tone / mixed_tone.max()) * 32767)

# число точек в normalized_tone
N = SAMPLE_RATE * DURATION

# 2 задание
# Используем быстрое преобразование Фурье
yf = fft(normalized_tone)
xf = fftfreq(N, 1 / SAMPLE_RATE)

# 3 задание
# Визуализируем в Python сгенерированный сигнал и его ряд Фурье. 
plt.title(" Сгенерированный сигнал")
plt.plot(x, y)
plt.show()

plt.title(" Ряд Фурье сгенерированного сигнала")
plt.plot(xf, np.abs(yf))
plt.show()
