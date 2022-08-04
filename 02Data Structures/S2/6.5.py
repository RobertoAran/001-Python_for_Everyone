text = 'X-DSPAM-Confidence:    0.8475'
sl_num = text.find("0")
sliced_text = slice(sl_num,33)
decim = float(text[sliced_text])
print(decim)

