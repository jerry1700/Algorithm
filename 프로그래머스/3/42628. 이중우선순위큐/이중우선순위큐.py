import heapq

def solution(operations):
    heap = []
    
    for op in operations:
        if op[0] == "I":
            heapq.heappush(heap, int(op[2:]))
        elif op == "D 1":
            heap = [-x for x in heap]
            heapq.heapify(heap)
            if heap:
                heapq.heappop(heap)
            heap = [-x for x in heap]
            heapq.heapify(heap)
        elif op == "D -1":
            if heap:
                heapq.heappop(heap)

    if not heap:
        return [0, 0]
    else:
        answer = [heap[0], heap[0]]
        heap = [-x for x in heap]
        heapq.heapify(heap)
        answer[0] = -heap[0]
        return answer
        