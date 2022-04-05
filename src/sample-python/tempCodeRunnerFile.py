
            print("The server did not respond with an HTTP OK response.")
            print(f"Response status: {response.status_code} - {response.reason}")
    except Exception as err:
        print(f"Unable to fetch vessel metrics: {err}")
