// https://leetcode.com/problems/count-artifacts-that-can-be-extracted

class Solution:
    def digArtifacts(self, n, artifacts, dig):

        #turn dig into set for easy (constant time) lookup later
        dig = set((r,c) for r,c in dig)

        count =0
        #check each position of the artifact
        for r1,c1, r2,c2 in artifacts:
            positions = set()
            for r in range(r1, r2+1):
                for c in range(c1, c2+1):
                    positions.add((r,c))

            #if all positions are dug up, add to result
            if all([pos in dig for pos in positions]):
                count+=1

        return count