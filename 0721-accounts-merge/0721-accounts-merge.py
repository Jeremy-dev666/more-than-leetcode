from collections import defaultdict

class UF:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        root_a, root_b = self.find(a), self.find(b)
        if root_a == root_b:
            return
        if self.rank[root_a] < self.rank[root_b]:
            self.parent[root_a] = root_b
        elif self.rank[root_a] > self.rank[root_b]:
            self.parent[root_b] = root_a
        else:
            self.parent[root_b] = root_a
            self.rank[root_a] += 1


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # 账号视为n个连通分量，有相同的email再执行合并
        n = len(accounts)
        uf = UF(n) 

        # 邮箱、账号索引的字典映射
        email_idx = defaultdict(int)  

        # 遍历, 合并具有相同邮箱的账号
        for idx, account in enumerate(accounts):
            for email in account[1:]:
                # 如果遍历到的邮箱已经放到字典里，那么说明有相同账号，需要合并
                if email in email_idx:
                    uf.union(idx, email_idx[email])
                else:
                    email_idx[email] = idx

        # 现在并查集中已经建立了共有父节点账号索引信息
        # 遍历email_idx字典，查找出每一封邮件对应的父节点，并建立 idx_email字典
        idx_email = defaultdict(list)  
        for email, idx in email_idx.items():
            idx_email[uf.find(idx)].append(email)

        # 最后一步，对账号下的邮件进行排序
        ans = []
        for idx, emails in idx_email.items():
            username = accounts[idx][0]
            sorted_emails = sorted(emails)
            cat = [username] + sorted_emails
            ans.append(cat)

        return ans

