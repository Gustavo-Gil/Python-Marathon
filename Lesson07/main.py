from indeed import search_ideed
from stackoverflow import search_so
from save import save_to_csv
import gspread


# busca
search = 'python'

#salva resultado do indeed
#result_indeed = search_ideed(search)
#salva resultado do indeed
result_so = search_so(search)
#result_indeed
#junta os resultados em all_results
all_resuts = result_so

#envia para salvar no csv
save_to_csv(all_resuts)

#conecta com as credenciais
gc = gspread.service_account(filename='credenciais.json')
sh = gc.open_by_key('1ZnXZrjbohKSyphlHR3sZs-OUob1YiBcnXY1d18NDVxs')
worksheet = sh.sheet1

#abre o csv
content = open('jobs.csv', 'r').read().encode('utf-8')
sheet = ('1ZnXZrjbohKSyphlHR3sZs-OUob1YiBcnXY1d18NDVxs')

#importa o csv para o shets
gc.import_csv(sheet, content)