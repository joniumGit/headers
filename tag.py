if __name__ == '__main__':
    import os
    import textwrap
    import datetime

    from create import VERSION_FORMAT

    created_at = datetime.date.today().strftime(VERSION_FORMAT)

    cmds = textwrap.dedent(
        f"""
        git config --global user.name 'joniumGit'
        git config --global user.email '52005121+joniumGit@users.noreply.github.com'
        git add .
        git commit -m "Automatically generated release {created_at}" || echo 'no changes to commit'
        git push || echo 'no changes to commit'
        git tag {created_at}
        git push --tags || echo 'no changes to commit'
        """
    ).splitlines()

    for cmd in cmds:
        os.system(cmd)
