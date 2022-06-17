import psycopg2

class Database():

    CRIA_TABELA_SEMESTRES = """
        create table if not exists semestres (
            ano int, 
            semestre int,
            check (semestre in (1,2)),
            primary key(ano, semestre)
        );
    """

    def __init__(self, host='localhost', database='pythonbd',
                 user='postgres', password='pgsql'):

        self.conexao = None

        try:
            self.conexao = psycopg2.connect(host=host,
                                            database=database,
                                            user=user,
                                            password=password)
            print('Conexao estabelecida com sucesso!')
        except Exception as erro:
            print(f'Erro ao conectar com o bd: {erro}')

    def create_table(self):
        try:
            with self.conexao:
                with self.conexao.cursor() as cursor:
                    cursor.execute(self.CRIA_TABELA_SEMESTRES)
                    print('Tabela criada com sucesso!')
        except Exception as erro:
            print(f'Erro ao criar a tabela {erro}')
