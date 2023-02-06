from flask import Flask, jsonify, request


app = Flask (__name__)

livros = [
    {
        "id":1,
        "titulo":"o senhor dos Aneis - a sociedade do ANEL",
        "autor ": "j.r.r tolkein "
        
    },   
    {
       
        "id":2,
        "titulo":"harry potter- pedra filosofal",
        "autor ": "j.k rollind "
        
    },   
        
        {
            
        "id":3,
        "titulo":"leonardo o bravo - volume 1",
        "autor ": "leorardo "
        
    },  
        
       ]
# efetuado a busca por livros consultar todos (get)
@app.route("/livros")
def obter_livros():
    return jsonify(livros)

#  EFETUADO A BUSTA POR ID (GET)
@app.route("/livros/<int:id>",methods=["GET"]) 
def obter_livros_por_id(id):
    for livro in livros:
        if livro.get("id") == id:
            return jsonify(livro)
    
    #EDITAR
    @app.route("/livros/<int:id>",methods=['PUT'])
    def editar_livro_id(id):
        livro_alterado = request.get_json()
        for indice,livro in enumerate(livros):
            if livro.get("id") == id:
                livro[indice].update(livro_alterado)
                return jsonify(livros[indice])
            
            # criar 
            @app.route("/livros/<int:id>",methods=["POST"])
            def incluir_novo_livro():
                novo_livro = request.get_json()
                livros.append(novo_livro)
                return jsonify(livros)
             
             #delete
            @app.route("/livros/<int:id>",methods=["DELETE"])
            def deletar_livro(id): 
                     for indice,livro in enumerate(livros):
                       if livro.get("id") == id:
                          del livros [indice]
                          return jsonify(livros)
            
                 
            
        

app.run(port=5000,host="localhost",debug=True)