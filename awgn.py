import numpy as np
import math

# 送信ビット数
bit_num = 10 ** 4

# 送信ビット列を生成
TX_bit = np.random.randint(0, 2, bit_num)
print(TX_bit)

noise = np.random.normal(0, np.sqrt(2), bit_num)
print(noise)

noisy_bit = TX_bit + noise
print(noisy_bit)

# 受信信号をビットに判定
RX_bit = np.zeros(bit_num)
RX_bit[noisy_bit >= 0] = 1
RX_bit[noisy_bit < 0] = 0
print(RX_bit)
print(~(RX_bit == TX_bit))

error = sum(~(RX_bit == TX_bit))/ bit_num
print(error)

t_error = math.erfc(1/2) / 2
print(t_error)