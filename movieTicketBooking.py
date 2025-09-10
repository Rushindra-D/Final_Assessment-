def book_seat(seat_number, booked_seats, total_seats):
    if seat_number > total_seats or seat_number < 1:
        return "Invalid seat number!"
    if seat_number in booked_seats:
        return f"Seat {seat_number} is already booked!"
    else:
        booked_seats.append(seat_number)
        return f"Seat {seat_number} has been successfully booked!"
def cancel_seat(seat_number, booked_seats):
    if seat_number in booked_seats:
        booked_seats.remove(seat_number)
        return f"Seat {seat_number} has been successfully cancelled!"
    else:
        return f"Seat {seat_number} is not booked!"
def available_seats(total_seats, booked_seats):
    available = [seat for seat in range(1, total_seats + 1) if seat not in booked_seats]
    return available
total_seats = 10
booked_seats = [2, 5, 7]
print("Available seats:", available_seats(total_seats, booked_seats))
book_seat_number = 3
print(book_seat(book_seat_number, booked_seats, total_seats))
print("Available seats:", available_seats(total_seats, booked_seats))
cancel_seat_number = 5
print(cancel_seat(cancel_seat_number, booked_seats))
print("Available seats:", available_seats(total_seats, booked_seats))
