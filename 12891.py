S, P = map(int, input().split())
dna = input().strip()
A, C, G, T = map(int, input().split())

num = 0
left = 0
right = P - 1
dic = {'A' : 0, 'C' : 0, 'G' : 0, 'T':0}
for i in dna[left:right+1]:
    dic[i] += 1

while right < S:
    if dic['A'] >= A and dic['C'] >= C and dic['G'] >= G and dic['T'] >= T:
        num+=1
    dic[dna[left]] -= 1
    left += 1
    right += 1
    if right < S:
        dic[dna[right]] += 1
print(num)