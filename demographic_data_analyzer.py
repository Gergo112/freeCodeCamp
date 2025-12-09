import pandas as pd

def calculate_demographic_data(print_data=True):
    # Read data
    df = pd.read_csv("adult.data.csv")

    # 1. Hány ember tartozik az egyes rasszokba?
    race_count = df["race"].value_counts()

    # 2. Férfiak átlagos életkora
    average_age_men = round(df[df["sex"] == "Male"]["age"].mean(), 1)

    # 3. Bachelor's diplomások aránya
    percentage_bachelors = round(
        (df["education"] == "Bachelors").mean() * 100, 1
    )

    # 4. Felsőfokú végzettség
    higher_education = df[df["education"].isin(["Bachelors", "Masters", "Doctorate"])]
    lower_education = df[~df["education"].isin(["Bachelors", "Masters", "Doctorate"])]

    # Felsőfokú végzettség + >50K
    higher_education_rich = round(
        (higher_education["salary"] == ">50K").mean() * 100, 1
    )

    # Nem felsőfokú végzettség + >50K
    lower_education_rich = round(
        (lower_education["salary"] == ">50K").mean() * 100, 1
    )

    # 5. Minimum munkaórák száma
    min_work_hours = df["hours-per-week"].min()

    # 6. Hány százaléka azoknak, akik minimum órát dolgoznak, keres >50K-t?
    min_workers = df[df["hours-per-week"] == min_work_hours]
    rich_percentage = round((min_workers["salary"] == ">50K").mean() * 100, 1)

    # 7. Melyik országban a legmagasabb a >50K kereset aránya?
    country_rich = (
        df[df["salary"] == ">50K"]["native-country"]
        .value_counts() /
        df["native-country"].value_counts() * 100
    )

    highest_earning_country = country_rich.idxmax()
    highest_earning_country_percentage = round(country_rich.max(), 1)

    # 8. India >50K legnépszerűbb foglalkozása
    top_IN_occupation = (
        df[(df["native-country"] == "India") & (df["salary"] == ">50K")]
        ["occupation"]
        .value_counts()
        .idxmax()
    )

    # Eredmények összegyűjtése
    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(
            f"Percentage with higher education that earn >50K: {higher_education_rich}%"
        )
        print(
            f"Percentage without higher education that earn >50K: {lower_education_rich}%"
        )
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(
            f"Highest percentage of rich people in country: {highest_earning_country_percentage}%"
        )
        print("Top occupation in India:", top_IN_occupation)

    # Visszatérés a tesztekhez
    return {
        "race_count": race_count,
        "average_age_men": average_age_men,
        "percentage_bachelors": percentage_bachelors,
        "higher_education_rich": higher_education_rich,
        "lower_education_rich": lower_education_rich,
        "min_work_hours": min_work_hours,
        "rich_percentage": rich_percentage,
        "highest_earning_country": highest_earning_country,
        "highest_earning_country_percentage": highest_earning_country_percentage,
        "top_IN_occupation": top_IN_occupation,
    }
