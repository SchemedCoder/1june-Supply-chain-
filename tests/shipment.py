import pandas as pd


def test_delay_calculation():

    df = pd.DataFrame(
        {
            "event_time": [
                "2026-01-01"
            ],
            "ingest_time": [
                "2026-01-04"
            ]
        }
    )

    df["event_time"] = pd.to_datetime(
        df["event_time"]
    )

    df["ingest_time"] = pd.to_datetime(
        df["ingest_time"]
    )

    delay = (
        df["ingest_time"]
        - df["event_time"]
    ).dt.days

    assert delay.iloc[0] == 3


def test_late_arrival():

    df = pd.DataFrame(
        {
            "delay": [4]
        }
    )

    assert (
        df["delay"].iloc[0] > 1
    )
