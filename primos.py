import os
from flask import Flask, jsonify, request
from math import sqrt

app = Flask(__name__)

@app.route('/')
def nao_entre_em_panico():

    n = 542
    primos = ""
    for i in range(1, n+1):
        divisores = 0
        for div in range(1, i+1):
            if i % div == 0:
                divisores += 1
        if divisores == 2:
            primos = primos + str(i) + ","
    return(primos)
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
