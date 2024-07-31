from api import db
from passlib.hash import pbkdf2_sha1
class Usuario(db.Model):
    __tablename__ = "usuario"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True,nullable=False)
    nome = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    senha=db.Column(db.String(255), nullable=False)

    def encriptar_senha(self):
        self.senha=pbkdf2_sha1.hash(self.senha)

    def ver_senha(self,senha):
        return pbkdf2_sha1.verify(senha,self.senha)