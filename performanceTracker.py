def get_available_seats(total_seats, booked_seats):
    return [seat for seat in range(1, total_seats + 1) if seat not in booked_seats]
def book_seat(booked_seats, seat):
    if seat in booked_seats:
        print(f"Seat {seat} is already booked.")
    else:
        booked_seats.append(seat)
def cancel_seat(booked_seats, seat):
    if seat in booked_seats:
        booked_seats.remove(seat)
    else:
        print(f"Seat {seat} is not booked.")
total_seats = 10
booked_seats = [2, 5, 7]
book_seat_num = 3
cancel_seat_num = 5

book_seat(booked_seats, book_seat_num)
cancel_seat(booked_seats, cancel_seat_num)

available = get_available_seats(total_seats, booked_seats)
print("Available seats:", available)
