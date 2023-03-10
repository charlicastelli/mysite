from django.db import models
from django.contrib.auth.models import User
from datetime import date

# Cria tabela Categoria banco de dados
# contém os campos e comportamentos essenciais
class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50, help_text="Nome da categoria")
    status = models.BooleanField(default=True, verbose_name="Ativo")

    def __str__(self):
        return self.nome

    class Meta:
        managed = True
        db_table = 'tab_categoria'
        verbose_name_plural=u"Categorias"

# Cria tabela Tipo imovel banco de dados
# contém os campos e comportamentos essenciais
class TipoImovel(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50, help_text="Nome.")
    status = models.BooleanField(default=True, verbose_name="Ativo")

    def __str__(self):
        return self.nome

    class Meta:
        managed = True
        db_table = 'tab_tipoImovel'
        verbose_name_plural=u'Tipos de imóveis'

# Cria tabela imovel banco de dados
# contém os campos e comportamentos essenciais
class Imovel(models.Model):
    id = models.AutoField(primary_key=True)
    tipoImovel = models.ForeignKey(TipoImovel, on_delete=models.CASCADE, blank=False)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, blank=False)
    nome = models.CharField(max_length=50, help_text="Nome")
    descricao = models.TextField(help_text="Descriçao do imóvel.")
    status = models.BooleanField(default=True, verbose_name="Ativo")

    def fotos(self):
        return Fotos.objects.filter(imovel_id=self.id)

    def __str__(self):
        return self.nome
    
    class Meta:
        managed = True
        db_table = 'tab_imovel'
        verbose_name_plural=u"Imóveis"

# Cria tabela fotos banco de dados
# contém os campos e comportamentos essenciais
class Fotos(models.Model):
    id = models.AutoField(primary_key=True)
    imovel = models.ForeignKey(Imovel, on_delete=models.CASCADE)
    foto = models.ImageField(upload_to="media/fotos/%Y/%m/%d", verbose_name="Foto", help_text="Escolha uma foto", blank=True)
    descricao = models.TextField(verbose_name="Descrição", help_text="Descrição")

    def __str__(self) -> str:
        return "%s - %s" % (self.imovel.nome, self.descricao)

    class Meta:
        managed = True
        db_table = 'tab_fotosImoveis'
        verbose_name_plural=u'Fotos dos imóveis'


# Cria tabela pessoas banco de dados
# contém os campos e comportamentos essenciais
class Pessoa(models.Model):

    SEXO_OPCOES = (
        ('M', 'Masculino'),
        ('F', 'Feminino')
    )

    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200, verbose_name="Nome", help_text="Nome completo")
    dataNascimento = models.DateField(verbose_name="Data de nascimento",
    help_text="dd/mm/aaaa")
    sexo = models.CharField(choices=SEXO_OPCOES, default="M", verbose_name="Sexo", help_text="Escolha o sexo", max_length=1)
    avatar = models.ImageField(upload_to="media/avatar/%Y/%m/%d",
    verbose_name="Avatar", help_text="Escolha uma imagem", blank=True, null=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.BooleanField(default=True, verbose_name="Ativo")

    def idade(self):
        today = date.today()
        return today.year - self.dataNascimento.year - ((today.month, today.day) < (self.dataNascimento.month, self.dataNascimento.day))

    def __str__(self):
        return self.nome

    class Meta:
        managed = True
        db_table = 'tab_pessoa'
        verbose_name_plural=u'Pessoas'

