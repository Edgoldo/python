# Complete the saveThePrisoner function below.
def saveThePrisoner(n, m, s):
    """
    Find the chair to warn. That is, the prisoner number to give the last sweet
    @date 28/07/2019
    @param <b>{int}</b> n Number of chairs ordered in a circle
    @param <b>{int}</b> m Number of sweets to deliver secuentially
    @param <b>{int}</b> s Chair to begin with delivering of sweets
    @return <b>{int}</b> Chair to be warned

    Constraints:
    1 <= n <= 1e9
    1 <= m <= 1e9
    1 <= s <= n
    """
    rest_sweets = s + (m - 1)
    if rest_sweets > n:
        if rest_sweets%n == 0:
            rest_sweets = n
        rest_sweets = rest_sweets%n
    rest_sweets = rest_sweets

    return rest_sweets

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        nms = input().split()

        n = int(nms[0])

        m = int(nms[1])

        s = int(nms[2])

        result = saveThePrisoner(n, m, s)
        
        print(str(result) + '\n')
