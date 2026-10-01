class Solution:
    def __init__(self): 
        self.adj_list: Dict[int, List[int]] = {}

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        in_degree: List[int] = [0] * numCourses

        for course, prereq in prerequisites: 
            if prereq not in self.adj_list: 
                self.adj_list[prereq] = []
            self.adj_list[prereq].append(course)
            in_degree[course] += 1

        queue = deque([])

        for course_index in range(len(in_degree)): 
            if in_degree[course_index] == 0: 
                queue.append(course_index)

        courses_taken = 0 

        while len(queue) > 0: 
            curr_course = queue.popleft()
            courses_taken += 1
            # if courses_taken == numCourses: 
            #     break
            for potential_course in self.adj_list.get(curr_course, []): 
                in_degree[potential_course] -= 1 
                if in_degree[potential_course] == 0: 
                    queue.append(potential_course)

        if courses_taken == numCourses: 
            return True 
        else: 
            return False

        
        