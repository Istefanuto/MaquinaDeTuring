import json 

class T_machine:
    def __init__(self, machine_data): 
        self.initial = machine_data["initial"] 
        self.final_state = machine_data["final_state"]
        self.blank_symbol = machine_data["blank_symbol"] 
        self.transitions = machine_data["transitions"]
    
    def get_action(self, state, symbol): 
        for transition in self.transitions:  
            if transition["from"] == state and transition["read"] == symbol:
                return (transition["to"], transition["write"], transition["move"]) 
            
        return None
    
    def simulate(self, tape): 
        current_state = self.initial[0] 
        current_index = 0 
        tape_list = list(tape) 

        while current_state not in self.final_state: 
            current_symbol = tape_list[current_index]

            action = self.get_action(current_state, current_symbol) 
            if action is None:  
                break 
            
        
            next_state, write_symbol, move_direction = action 

            tape_list[current_index] = write_symbol 

            if move_direction == "R": 
                current_index += 1
            elif move_direction == "L":
                current_index -= 1

            if current_index < 0: 
                tape_list.insert(0, self.blank_symbol)
                current_index = 0
            if current_index >= len(tape_list):
                tape_list.append(self.blank_symbol) 

            current_state = next_state

        if current_state in self.final_state: 
            print("1") 
            return "".join(tape_list).strip() 
            
        else:
            print("0") 
            return "".join(tape_list).strip()  

        
def machine_file(file_path): 
    try:
        with open(file_path, 'r') as json_file: 
            machine_data = json.load(json_file)
        return machine_data
    except FileNotFoundError:
        print(f"Arquivo {file_path} não encontrado.")
        return None
    except json.JSONDecodeError:
        print(f"Erro ao decodificar o arquivo JSON {file_path}. Verifique o formato.")
        return None

def main(): #Função main 
    file_aut_path = 'arquivo.json' 

    machine_data = machine_file(file_aut_path) 
    if machine_data is None:
        return 

    machine = T_machine(machine_data) 

   
    input_file_path = "entrada.txt"

    try:
        with open(input_file_path, "r") as file:
            input_tapes = file.readlines() 
    except FileNotFoundError:
        print("Arquivo de entrada não encontrado.")
        return

    print("Simulação iniciada:")
    with open("saida.txt", "w") as output_file: 
        for tape in input_tapes:
            tape = tape.strip()  
            result_tape = machine.simulate(tape)
            output_file.write(f"{result_tape}\n")  
    print("Fim da simulação")

if __name__ == "__main__":
    main()
 