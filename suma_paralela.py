import time
import multiprocessing
import random

# --- Configuración del Problema ---
# Reducimos el tamaño del arreglo. Para operaciones con listas nativas,
# 5 millones de elementos es un tamaño donde el overhead de multiprocessing
# podría ser menos dominante que el cálculo real, permitiendo ver speedup.
ARRAY_SIZE = 5_000_000 # Reducido a 5 millones para listas nativas.

# Función que cada proceso ejecutará para sumar los cuadrados de una porción del arreglo
def sum_squares_portion(arr_portion):
    """Calcula la suma de los cuadrados de los elementos en una porción del arreglo."""
    local_sum = 0
    for x in arr_portion:
        local_sum += x * x # Operación más intensiva que solo una suma
    return local_sum

def run_multiprocessing_test(num_processes_to_test):
    print("--- Test con Multiprocessing (Suma de Cuadrados - Listas Nativas) ---")
    print(f"Resultados para un arreglo de tamaño: {ARRAY_SIZE}")
    print("---------------------------------------------------")
    print("| Procesos | Tiempo (s) | Speedup | Eficiencia |")
    print("---------------------------------------------------")

    # Generar el arreglo grande usando listas de Python y random
    print(f"Generando arreglo de {ARRAY_SIZE} elementos (esto puede tardar)...")
    # Generar números más pequeños para evitar que los cuadrados se desborden si usáramos tipos fijos
    # aunque Python integers manejan tamaño arbitrario
    data_array = [random.randint(0, 100) for _ in range(ARRAY_SIZE)]
    print("Arreglo generado.")

    sequential_time = 0.0

    # Realizar una verificación secuencial al final para asegurar la corrección del resultado.
    # No es parte de la medición de rendimiento de la tabla, solo una verificación.
    # sum_check = sum_squares_portion(data_array)
    # print(f"Suma de cuadrados de verificación secuencial: {sum_check}")


    for num_processes in num_processes_to_test:
        current_total_sum = 0 # Reiniciar la suma para cada prueba
        start_time = time.time()
        
        # Caso de un solo proceso (suma de cuadrados secuencial)
        if num_processes == 1:
            current_total_sum = sum_squares_portion(data_array)
        else:
            # Dividir el arreglo en trozos para cada proceso
            chunk_size = ARRAY_SIZE // num_processes
            chunks = []
            for i in range(num_processes):
                start_index = i * chunk_size
                end_index = (i + 1) * chunk_size
                if i == num_processes - 1: # El último chunk toma el resto
                    end_index = ARRAY_SIZE
                chunks.append(data_array[start_index:end_index])
            
            with multiprocessing.Pool(processes=num_processes) as pool:
                partial_sums = pool.map(sum_squares_portion, chunks)
                current_total_sum = sum(partial_sums) # Sumar las sumas parciales

        end_time = time.time()
        elapsed_time = end_time - start_time

        if num_processes == 1:
            sequential_time = elapsed_time

        speedup = sequential_time / elapsed_time
        efficiency = speedup / num_processes

        print(f"| {num_processes:<8} | {elapsed_time:<10.6f} | {speedup:<7.2f} | {efficiency:<10.2f} |")
    print("---------------------------------------------------\n")
    print(f"Suma de cuadrados total (verificación): {current_total_sum}")


# --- Ejecución del Test principal ---
if __name__ == '__main__':
    # Lista de procesos a probar. Ajusta según los núcleos de tu CPU.
    # Es común ir hasta el doble de núcleos lógicos para ver el comportamiento.
    num_processes_to_test = [1, 2, 4, 8]
    # Si tienes 4 núcleos físicos/8 lógicos, probar hasta 8 o 16 tiene sentido.
    # Ejemplo: num_processes_to_test = [1, 2, 4, 6, 8, 10, 12, 14, 16]

    run_multiprocessing_test(num_processes_to_test)