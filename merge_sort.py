def merge_sort(individuals_fitness_dict):
    def merge(left, right):
        if len(left) == 0:
            return right
        
        if len(right) == 0:
            return left
        
        result = []
        index_left = index_right = 0
        while len(result) < len(left) + len(right):
            if individuals_fitness_dict[left[index_left]] >= individuals_fitness_dict[right[index_right]]:
                result.append(left[index_left])
                index_left += 1
            else:
                result.append(right[index_right])
                index_right += 1

            if index_right == len(right):
                result += left[index_left:]
                break
            if index_left == len(left):
                result += right[index_right:]
                break
        return result

    def start_merge(individuals):
            if len(individuals) < 2:
                return individuals
            
            midpoint = len(individuals) // 2
            
            return merge(
                left=start_merge(individuals[:midpoint]),
                right=start_merge(individuals[midpoint:]))
    
    individuals = list(individuals_fitness_dict.keys())

    return start_merge(individuals)
    