from github import Github
from datetime import datetime, timedelta


class Model:

    def __init__(self, token, repositoryName):
        self.token = token
        self.repositoryName = repositoryName

    def get_offline_data(self):
        historys = []
        stargazers = self.get_starred_strangers()

        for i, people in enumerate(stargazers):
            historys.append(datetime.timestamp(people.starred_at))
            if i % 5000 == 0:
                with open("result" + str(i) + ".txt", "w") as f:
                    f.writelines("\n".join('%s' % a for a in historys))
                    historys = []

    def get_online_data_per_hour(self):
        historys = []
        stargazers = self.get_starred_strangers()
        starred_at_list = [datetime.timestamp(people.starred_at) for people in stargazers]
        starred_at_list.sort(reverse=True)

        timestamp_one_hour_ago = datetime.timestamp((datetime.now() - timedelta(hours=1)))

        for ts in starred_at_list:
            if ts >= timestamp_one_hour_ago:
                historys.append(ts)
            else:
                break
        with open("resultRecentOneHour.txt", "w") as f:
            f.writelines("\n".join('%s' % a for a in historys))
            historys = []


    def get_starred_strangers(self):
        g = Github(self.token)
        repo = g.get_repo(self.repositoryName)  # 仓库名
        return repo.get_stargazers_with_dates()
