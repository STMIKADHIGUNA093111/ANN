import math, random
random.seed(404)

def bersihberkas(berkas):
    data = []
    #ulang per baris
    for baris in open(berkas):
        #buang karakter \n
        baris = baris.replace("\n","")

        #baris kosong dilewati
        if(baris == ""):
            continue

        #split baris berdasarkan karakter koma (,)
        barisdata = baris.split(",")

        #masukkan hasil split ke dalam list data
        data.append(barisdata)
    return data

def bagidata(data, pembagi, fitur):
    out = {"trfitur":[],"trpred":[],"tefitur":[],"tepred":[]}

    #acak data
    random.shuffle(data)

    #bagi berdasarkan train, test dan jumlah fitur
    out['trfitur'] = [d[:fitur] for d in data[:pembagi]]
    out['trpred']  = [d[fitur:] for d in data[:pembagi]]
    out['tefitur'] = [d[:fitur] for d in data[pembagi+1:]]
    out['tepred']  = [d[fitur:] for d in data[pembagi+1:]]

    return out

def buatbobot(arsitektur):
    bobot = []

    #banyak himpunan bobot
    for i in range(len(arsitektur)-1):
        b = []
        for j in range(arsitektur[i]):
            d = []
            for k in range(arsitektur[i+1]+1):
                d.append(random.uniform(-1,1))
            b.append(d)
        bobot.append(b)
    print(bobot)

def sigmoid(t):
    return 1/(1+math.exp(-t))


def akumulasi(list):
    a = 0.0
    for i in range(len(list)):
        a = a + float(list[i])
    return a

def feedforward(data, bobot, arsitektur):
    return 0
