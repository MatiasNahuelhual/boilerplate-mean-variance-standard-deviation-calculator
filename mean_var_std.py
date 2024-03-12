import numpy as np

def calculate(numbers):
    # Verificar si la lista tiene exactamente 9 elementos
    if len(numbers) != 9:
        raise ValueError("La lista debe contener nueve números")
    
    # Convertir la lista en una matriz de 3x3
    matrix = np.array(numbers).reshape(3, 3)
    
    # Calcular las estadísticas
    mean = [np.mean(matrix, axis=0).tolist(), np.mean(matrix, axis=1).tolist(), np.mean(matrix).tolist()]
    variance = [np.var(matrix, axis=0).tolist(), np.var(matrix, axis=1).tolist(), np.var(matrix).tolist()]
    std_dev = [np.std(matrix, axis=0).tolist(), np.std(matrix, axis=1).tolist(), np.std(matrix).tolist()]
    max_val = [np.max(matrix, axis=0).tolist(), np.max(matrix, axis=1).tolist(), np.max(matrix).tolist()]
    min_val = [np.min(matrix, axis=0).tolist(), np.min(matrix, axis=1).tolist(), np.min(matrix).tolist()]
    sum_val = [np.sum(matrix, axis=0).tolist(), np.sum(matrix, axis=1).tolist(), np.sum(matrix).tolist()]
    
    # Crear el diccionario de resultados
    result = {
        'mean': mean,
        'variance': variance,
        'standard deviation': std_dev,
        'max': max_val,
        'min': min_val,
        'sum': sum_val
    }
    
    return result
