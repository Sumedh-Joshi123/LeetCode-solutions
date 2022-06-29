class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        sortedPeople = sorted(people, key=(lambda person: (-person[0], person[1])))
        result = []
        for person in sortedPeople:
            result.insert(person[1], person)

        return result