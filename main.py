from prediction import predict_delivery_time


def main():

    print("\n" + "=" * 45)
    print("     FOOD DELIVERY TIME PREDICTION SYSTEM")
    print("=" * 45)

    try:
        distance = float(input("\nEnter delivery distance (km): "))
        weather = input("Enter weather (Clear/Rainy/Windy): ").strip()
        traffic = input("Enter traffic (Low/Medium/High): ").strip()
        time_of_day = input("Enter time of day (Morning/Afternoon/Evening/Night): ").strip()
        vehicle = input("Enter vehicle type (Bike/Scooter/Car): ").strip()
        preparation_time = float(input("Enter preparation time (minutes): "))
        courier_experience = float(input("Enter courier experience (years): "))

        result = predict_delivery_time(
            distance,
            weather,
            traffic,
            time_of_day,
            vehicle,
            preparation_time,
            courier_experience
        )

        print("\n" + "=" * 45)
        print("          PREDICTION RESULT")
        print("=" * 45)
        print(f"Estimated delivery time: {result} minutes")
        print("=" * 45)

    except ValueError:
        print("\nInvalid input. Please enter valid numerical values.")

    except Exception as error:
        print("\nPrediction error:", error)


if __name__ == "__main__":
    main()


