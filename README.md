# Schmidt Samoa implementation on Python
Python-Schmidt-Samoa is a pure-Python Schmidt samoa cryptosystem implementation. It supports encryption, decryption and key generation.

# Installation
Just working on Python 2 for now.(Tested on Python 2.7.13)

```
$ git clone https://github.com/blackvkng/python-schmidt-samoa && cd python-schmidt-samoa
$ sudo python2 setup.py install
```

# Usage

### Key generation
You can use `generateKey` function to generate a bits public and private key.

```python
>>> import schmidtSamoa as SS
>>> pubkey, privkey = SS.generate(512)
>>>
>>> pubkey
1444878015013177823624100543513398435632428994235263623602529883172627989797467997663180871673348920773178609625102140352091212170742104792296825511219922572694951403154361565059577952500886161821870858395240354290650349358660458553003837770019254142733356894262482148903247211340450194391785799775743985802831453380332722061436873138691741579860020235865989503555421366712016746113983206544714672316995020666933387786437648875094654653767747792256028788236670411L
>>>
>>> privkey[0]
56100117254717097623225041506997826808360925819376993138679171846204466539281766936714496279276841177335519328207811535604357403289595821603300401442839412412442086848233192648081814884436165150051766115112120475019183921079804398614650992671169755421855505487780830183538299485163222183099221131154450924851L
>>>
>>> privkey[1] # result of p * q
120469076346364638032191882513141954441443561871588689393851975062131751993733655854800327647259548210669476278226659011703474443910889849133370782457013622108257525628519431831104509759934842439925540468106721605898573607993172401605507279379080622852029661496409886020364728775389129029329836116531920437943L
```

### Encryption and Decryption
```python
>>> import schmidtSamoa as SS
>>> pubkey, privkey = SS.generate(16)
>>>
>>> message = "test message"
>>>
>>> ciphertext = SS.encrypt(message, pubkey)
>>> print ciphertext
MzE5NDE0Nzc5Nzg5MDcgMTA5NDIwMjg3MTUzOTUxIDk1OTAwMDQxNDExNzcxIDMxOTQxNDc3OTc4OTA3IDE1NTAxMjYzMTM4MzYxOCAxMDM2MDk2NjU3MjM3MDMgMTA5NDIwMjg3MTUzOTUxIDk1OTAwMDQxNDExNzcxIDk1OTAwMDQxNDExNzcxIDkyNzcxMTcyNTIwMTIgMTM0NTY0NDc1Njg5NzgwIDEwOTQyMDI4NzE1Mzk1MQ==
>>>
>>> plaintext = SS.decrypt(ciphertext, privkey[0], privkey[1])
>>> print plaintext
test message
```
