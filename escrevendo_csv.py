import csv
with open('fix/produtos.csv', 'w') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow([
        'produto', 'ncm', 'importado', 'preco', 'estoque', 'estoque_minimo'
    ])

    rows = [
        ['Apontador', 14669768, True, 15.54, 125, 30],
        ['Caderno 100 folhas', 44716505, True, 6.52, 120, 10],
        ['Caderno capa dura 200 folhas', 61556783, False, 24.46, 92, 20],
        ['Caneta esferográfica azul', 80951350, False, 11.42, 138, 20],
        ['Caneta esferográfica preta', 19009230, True, 3.71, 148, 40],
        ['Caneta esferográfica vermelha', 62358012, False, 13.74, 186, 50],
        ['Durex', 52181421, False, 7.43, 11, 20],
        ['Giz de cera 12 cores', 54194976, True, 23.66, 46, 10],
        ['Lapiseira 0.3 mm', 14122061, False, 10.76, 141, 40],
        ['Lapiseira 0.5 mm', 44284736, True, 0.71, 199, 40],
        ['Lapiseira 0.7 mm', 40347035, False, 11.28, 192, 50],
        ['Lápis de cor 24 cores', 73784057, False, 13.80, 103, 10],
        ['Lápis', 67410825, True, 3.27, 154, 20],
        ['Papel sulfite A4 pacote 100 folhas', 31000281, False, 18.26, 197, 20],
        ['Pasta elástica', 85605700, True, 7.10, 48, 40],
        ['Tesoura', 13750972, False, 9.68, 77, 10],
        ['Agasalho de moleton', 12892188, False, 19.3, 138, 40],
        ['Arquivador de 40 mm', 82331818, False, 14.42, 63, 50],
        ['Base para tinta', 98108254, False, 41.38, 95, 10],
        ['Bloco de papel cavalinho A4', 62276666, False, 5.67, 65, 30],
        ['Borracha', 81660090, False, 15.3, 103, 10],
        ['Borracha branca', 52498240, False, 21.23, 97, 30],
        ['Caderno de música', 16356845, False, 3.08, 43, 40],
        ['Caderno pautado', 11848921, False, 22.12, 31, 30],
        ['Caderno quadriculado', 42473200, False, 15.75, 158, 50],
        ['Cadernos pautados', 97081452, False, 2.55, 175, 50],
        ['Calculadora', 39854288, False, 17.84, 174, 40],
        ['Calculadora não gráfica com funções trigonométricas',
         60271477, False, 6.33, 107, 50],
        ['Calções', 20263760, False, 13.68, 66, 50],
        ['Camiseta', 30533013, False, 1.43, 79, 20],
        ['Capa arquivadora de desenhos A3', 80951670, False, 35.88, 131, 30],
        ['Chinelos de banho', 38334781, False, 11.3, 49, 40],
        ['Compasso', 17234430, False, 15.24, 36, 50],
        ['Conjunto de guaches', 58697819, False, 8.6, 91, 30],
        ['Corretor de fita', 64799144, False, 21.69, 14, 40],
        ['Esferográficas azul', 16190360, False, 1.19, 133, 50],
        ['Esferográficas preta', 43330220, False, 2.49, 145, 20],
        ['Esferográficas verde', 50335982, False, 23.43, 63, 20],
        ['Esferográficas vermelha', 81778926, False, 23.43, 71, 10],
        ['Esquadro de 45º', 53394301, False, 34.55, 86, 40],
        ['Estojo', 23218501, False, 10.37, 104, 10],
        ['Fato de treino', 45333495, False, 7.35, 39, 30],
        ['Flauta de bisel', 76416059, False, 5.13, 37, 20],
        ['Lápis (H HB B e 6B)', 95686853, False, 4.28, 194, 50],
        ['Lápis de cera', 25171646, False, 3.16, 20, 50],
        ['Lápis de cor', 77359983, False, 1.62, 116, 20],
        ['Lápis HB', 35551053, False, 8.3, 48, 30],
        ['Marcadores', 20881967, False, 5.51, 159, 10],
        ['Mochila', 94164016, False, 8.61, 65, 20],
        ['Pano de limpeza', 35250660, False, 2.3, 53, 40],
        ['Pen drive', 52062047, False, 17.68, 139, 20],
        ['Pincel n. 2', 89510296, False, 8.4, 47, 30],
        ['Pincel n. 8', 12462499, False, 9.19, 26, 20],
        ['Produtos de higiene', 10321310, False, 22.71, 40, 40],
        ['Régua de 20 cm', 11168615, False, 21.06, 43, 10],
        ['Régua de 50 cm', 28135120, False, 39.86, 78, 40],
        ['Saco para o equipamento', 29641340, False, 25.15, 57, 20],
        ['Sapatilhas de desporto', 24190558, False, 12.44, 31, 30],
        ['Stick de cola', 34110222, False, 10.41, 187, 10],
        ['Toalha', 42752411, False, 23.03, 159, 30],
        ['Transferidor', 40709929, False, 26.92, 32, 20],
        ['Tubo de cola', 41795932, False, 8.27, 176, 10],
    ]
    csv_writer.writerows(rows)
