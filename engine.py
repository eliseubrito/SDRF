import face_recognition as fr
import pathlib
import json
import os

def registrar_usuario(nome:str,cargo:str,idade:str):
    fname = 'db.json'
    data = [{
        'nome': nome,
        'cargo': cargo,
        'idade': idade
        }]
    if os.path.exists(fname):
        with open(fname,"r") as f:
            loaded = json.load(f)
            loaded.append({
        'nome': nome,
        'cargo': cargo,
        'idade': idade
        })
    else:
        loaded = data

    with open(fname,"w") as f:
        json.dump(loaded,f, indent=4)

def reconhece_face(url_foto:str):
    foto = fr.load_image_file(url_foto)
    rosto = fr.face_encodings(foto)
    # if(len(rostos) > 0):
    #     return True, rostos
    # print(True,rosto[0])
    return rosto

# reconhece_face("./images/1.jpg")

def get_infos():
    users = lerJson()
    print(len(users))

    nome = []
    cargo = []
    idade = []

    for id in range(len(users)):
        rosto = reconhece_face(f'./images/{id}.jpg')
        if(rosto):
            nome.append(users[id]['nome'])
            cargo.append(users[id]['cargo'])
            idade.append(users[id]['idade'])
            print (nome,cargo, idade)

    return nome, cargo, idade

def get_rostos():
    nomes_bd = get_infos()
    rostos_conhecidos = []
    nomes_dos_rostos = []

    for id in range(len(nomes_bd)):
        rosto = reconhece_face(f'./images/{id}.jpg')
        if(rosto):
            rostos_conhecidos.append(rosto[0])
            nomes_dos_rostos.append(nomes_bd[0][id])
    
    print(rostos_conhecidos, nomes_dos_rostos)
    return rostos_conhecidos, nomes_dos_rostos

def lerJson():
    f = open('db.json')
    data = json.load(f)
    f.close()
    # print(data)
    return data

def contarArquivos():
    initial_count = 0
    for path in pathlib.Path("./images").iterdir():
        if path.is_file():
            initial_count += 1
    print(initial_count)
    return initial_count

# face = reconhece_face("./images/2.jpg")
# print(face)
# registrar_usuario("Chris Wood","Ator",35)
# registrar_usuario("Ana","Gostosa",31)
# lerJson()
# get_infos()

# get_infos()

# get_rostos()