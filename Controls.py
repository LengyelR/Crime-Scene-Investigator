import numpy as np
from numpy.linalg import inv
from numpy.linalg import solve
from Enums import Const


def click(event, canvas1, canvas2, data):
    data.canvas1_counter += 1

    if data.canvas1_counter <= 4:
        data.x_list.append(event.x)
        data.y_list.append(event.y)
        canvas1.create_oval(event.x + Const.RADIUS, event.y + Const.RADIUS,
                            event.x - Const.RADIUS, event.y - Const.RADIUS,
                            fill="blue")

    elif data.canvas1_counter == 5 and data.canvas2_counter >= 4:
        data.x_list.append(event.x)
        data.y_list.append(event.y)

        # We can index in the arrays without worries because of the elif
        data.A = np.array([[data.x_list[0], data.x_list[1], data.x_list[2]],
                           [data.y_list[0], data.y_list[1], data.y_list[2]],
                           [1, 1, 1]])
        data.b = np.array([data.x_list[3],
                           data.y_list[3],
                           1.])

        data.chosen_point = np.array([data.x_list[4],
                                      data.y_list[4],
                                      1])
        data.canvas1_chosen_point = canvas1.create_oval(data.chosen_point[0] + Const.RADIUS,
                                                        data.chosen_point[1] + Const.RADIUS,
                                                        data.chosen_point[0] - Const.RADIUS,
                                                        data.chosen_point[1] - Const.RADIUS,
                                                        fill="red")
        transform(data, canvas2)

    else:  # We already have a previous chosen point
        data.x_list[4] = event.x
        data.y_list[4] = event.y
        data.chosen_point = np.array([data.x_list[4],
                                      data.y_list[4],
                                      1])

        canvas1.coords(data.canvas1_chosen_point,
                       data.chosen_point[0] + Const.RADIUS, data.chosen_point[1] + Const.RADIUS,
                       data.chosen_point[0] - Const.RADIUS, data.chosen_point[1] - Const.RADIUS)
        transform(data, canvas2, replace=True)


def click2(event, canvas, data):
    data.canvas2_counter += 1

    if data.canvas2_counter < 4:
        data.x_list2.append(event.x)
        data.y_list2.append(event.y)
        canvas.create_oval(event.x + Const.RADIUS, event.y + Const.RADIUS,
                           event.x - Const.RADIUS, event.y - Const.RADIUS,
                           fill="blue")

    elif data.canvas2_counter == 4:
        data.x_list2.append(event.x)
        data.y_list2.append(event.y)
        canvas.create_oval(event.x + Const.RADIUS, event.y + Const.RADIUS,
                           event.x - Const.RADIUS, event.y - Const.RADIUS,
                           fill="blue")

        data.b2 = np.array([event.x,
                            event.y,
                            1.])
        data.A2 = np.array([[data.x_list2[0], data.x_list2[1], data.x_list2[2]],
                            [data.y_list2[0], data.y_list2[1], data.y_list2[2]],
                            [1, 1, 1]])


def transform(data, canvas, replace=False):
    x = solve(data.A, data.b)
    x2 = solve(data.A2, data.b2)

    a1 = data.A[:, 0] * x[0]
    b1 = data.A[:, 1] * x[1]
    c1 = data.A[:, 2] * x[2]

    a2 = data.A2[:, 0] * x2[0]
    b2 = data.A2[:, 1] * x2[1]
    c2 = data.A2[:, 2] * x2[2]

    L1 = inv(np.array([a1, b1, c1]).transpose())
    L2 = np.array([a2, b2, c2]).transpose()
    L = np.dot(L2, L1)

    result = np.dot(L, data.chosen_point)
    result = result / result[2]

    if not replace:
        data.transformed_point = canvas.create_oval(result[0] + Const.RADIUS, result[1] + Const.RADIUS,
                                                    result[0] - Const.RADIUS, result[1] - Const.RADIUS,
                                                    fill="red")
    else:
        canvas.coords(data.transformed_point,
                      result[0] + Const.RADIUS, result[1] + Const.RADIUS,
                      result[0] - Const.RADIUS, result[1] - Const.RADIUS)
