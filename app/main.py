class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


class BaseRobot:
    def __init__(self, name: str, weight: int, coord: None) -> None:
        if coord is None:
            coord = [0, 0, 0]
        self.name = name
        self.weight = weight
        self.coord = coord

    def go_forward(self, step: int = 1) -> None:
        if step > 0:
            self.coord = self.coord.copy()
            self.coord.copy()[1] += step

    def go_back(self, step: int = 1) -> None:
        if step < 0:
            self.coord = self.coord.copy()
            self.coord.copy()[1] += step

    def go_right(self, step: int = 1) -> None:
        if step > 0:
            self.coord = self.coord.copy()
            self.coord.copy()[0] += step

    def go_left(self, step: int = 1) -> None:
        if step < 0:
            self.coord = self.coord.copy()
            self.coord.copy()[0] += step

    def get_info(self) -> str:
        return f"Robot: {self.name}, Weight: {self.weight}"


class FlyingRobot(BaseRobot):
    def __init__(self, name: str, weight: int, coord: None) -> None:
        super().__init__(name, weight, coord)

    def go_up(self, step: int = 1) -> None:
        if step > 0:
            self.coord = self.coord.copy()
            self.coord.copy()[2] += step

    def go_down(self, step: int = 1) -> None:
        if step < 0:
            self.coord = self.coord.copy()
            self.coord.copy()[2] += step


class DeliveryDrone(FlyingRobot):
    def __init__(self, name: str, weight: int, coord: None,
                 max_load_weight: int, current_load: None = 0) -> None:
        self.max_load_weight = max_load_weight
        self.current_load = current_load
        super().__init__(name, weight, coord)

    def hook_load(self, cargo: Cargo) -> None:
        if self.current_load is None and cargo.weight < self.max_load_weight:
            self.current_load = cargo.weight

    def unhook_load(self) -> None:
        self.current_load = None
