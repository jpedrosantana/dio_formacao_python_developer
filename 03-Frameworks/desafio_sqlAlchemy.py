from sqlalchemy import Column, Float, ForeignKey, Integer, String, create_engine, inspect, select
from sqlalchemy.orm import relationship, declarative_base, Session

Base = declarative_base()

class Cliente(Base):
    __tablename__ = "client_table"
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    cpf = Column(String(9))
    endereco = Column(String(9))

    #Adicionar relacionamento
    #https://docs.sqlalchemy.org/en/20/orm/basic_relationships.html
    conta = relationship(
        'Conta', back_populates='cliente', cascade='all, delete-orphan'
    )

    def __repr__(self):
        return f"Cliente (id={self.id}, nome={self.nome}, cpf={self.cpf})"

class Conta(Base):
    __tablename__ = "bank_account"
    id = Column(Integer, primary_key=True)
    tipo = Column(String)
    agencia = Column(String)
    num = Column(Integer)
    id_cliente = Column(Integer, ForeignKey("client_table.id"), nullable=False)
    saldo = Column(Float)

    #Adicionar relacionamento
    cliente = relationship(
        'Cliente', back_populates='conta'
    )

    def __repr__(self):
        return f"Conta (id={self.id}, tipo={self.tipo}, agencia={self.agencia}, número={self.num}, saldo={self.saldo})"

print(Cliente.__tablename__)
print(Conta.__tablename__)

#criando conexão com o banco
engine = create_engine("sqlite://")

#criando as classes como tabelas no banco
Base.metadata.create_all(engine)

#criando o esquema do banco de dados
inspector_engine = inspect(engine)

print("\n", inspector_engine.has_table)
print("\n", inspector_engine.get_table_names)
print("\n", inspector_engine.default_schema_name)

with Session(engine) as session:
    #Definindo objetos para instanciar no banco
    joao = Cliente(
        #id='001',
        nome='João Paulo',
        cpf='57214022910',
        endereco='R. Teste',
        conta=[Conta(
            tipo='Corrente',
            agencia='314',
            num='74429',
            saldo=620.35
        ),Conta(
            tipo='Poupança',
            agencia='211',
            num='56623',
            saldo=1000.00
        )]
    )

    sandy = Cliente(
        #id='001',
        nome='Sandy',
        cpf='35092800799',
        endereco='R. Teste 2',
        conta=[Conta(
            tipo='Corrente',
            agencia='211',
            num='21136',
            saldo=550.6
        )]
    )

    #Persiste os dados no banco
    session.add_all([joao, sandy])
    session.commit()

print("\nRecuperando clientes a partir de condição de filtragem")
stmt = select(Cliente).where(Cliente.nome.in_(["João Pedro"]))
for user in session.scalars(stmt):
    print(user)

print("\nRecuperando as contas correntes")
stmt_account = select(Conta).where(Conta.tipo.in_(['Corrente']))
for address in session.scalars(stmt_account):
    print(address)

print("\nRecuperando contas ordenadas do maior para o menor saldo")
order_stmt = select(Conta).order_by(Conta.saldo.desc())
for result in session.scalars(order_stmt):
    print(result)