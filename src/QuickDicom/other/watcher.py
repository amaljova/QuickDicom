'''
@ author: Amal Joseph Varghese
@ email: amaljova@gmail.com
@ github: https://github.com/amaljova
@ date: 12 June 2023
'''


from pathlib import Path
import pickle

class Watcher:
    def __init__(self, dir_name: Path):
        self.dir_name = Path(dir_name)
        try:
            self.old_paths, self.old_path_names = self.getState()
        except:
            self.old_paths = self.getPaths(self.dir_name)
            self.old_path_names = set(self.old_paths)
        self.scan()

    def getState(self) -> tuple:
        with open("watcherState.pkl", "rb") as f:
            state = pickle.load(f)
            return state

    def getPaths(self, path: Path) -> dict:
        path_dict = dict()
        for x in Path(self.dir_name).rglob("*"):
            try:
                path_dict[str(x)] = (x.stat().st_ctime, x.is_dir())
            except FileNotFoundError:
                pass
        return path_dict
    
    def scan(self) -> None:

        new_paths = self.getPaths(self.dir_name)
        new_path_names = set(new_paths)

        self.created = new_path_names - self.old_path_names
        self.deleted = self.old_path_names - new_path_names
        self.modified = set()
        for name in self.old_path_names & new_path_names:
            new_time, is_dir = new_paths[name]
            old_time, _ = self.old_paths[name]
            if new_time != old_time:
                self.modified.add(name)


        self.old_paths = new_paths
        self.old_path_names = new_path_names
        self.pickleState()
        
    def pickleState(self) -> None:
        state = (self.old_paths, self.old_path_names)
        with open("watcherState.pkl", "wb") as f:
            pickle.dump(state, f)

    def getCreated(self) -> list:
        return(list(self.created))
    
    def getDeleted(self) -> list:
        return(list(self.deleted))
    
    def getModified(self) -> list:
        return(list(self.modified))
    
