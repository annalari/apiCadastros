from django.db import models

class Pais(models.Model):
    descricao = models.CharField(max_length=45, null=False)
    
    def __str__(self):
        return self.descricao

class Estado(models.Model):
    descricao = models.CharField(max_length=45, null=False)

    def __str__(self):
        return self.descricao

class Cidade(models.Model):
    descricao = models.CharField(max_length=45, null=False)
    pais = models.ForeignKey(Pais,null=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.descricao

class Bairro(models.Model):
    descricao = models.CharField(max_length=45, null=False)
    pais = models.ForeignKey(Pais,null=False, on_delete=models.CASCADE)
    cidade = models.ForeignKey(Cidade,null=False, on_delete=models.CASCADE) 

    def __str__(self):
        return self.descricao

class Endereco(models.Model):
    numero = models.IntegerField()
    complemento = models.CharField(max_length=45)
    cep = models.BigIntegerField(max_length=8)
    pais = models.ForeignKey(Pais,null=False, on_delete=models.CASCADE)
    cidade = models.ForeignKey(Cidade,null=False, on_delete=models.CASCADE) 
    bairro = models.ForeignKey(Bairro,null=False, on_delete=models.CASCADE)


class Pessoa(models.Model):
    nome = models.CharField(max_length=45, null=False)
    cpf = models.IntegerField(max_length=11, null=False)
    rg = models.IntegerField(max_length=20, null=False)
    dataNascimento = models.DateField(auto_now=False, null=False)
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome