#!/usr/bin/env python3
"""
Simple templating program
"""


def generate_invitations(template, attendees):
    """
    Generates invitation files from a template and a list of attendees.
    """

    # Check template type
    if not isinstance(template, str):
        print("Error: template must be a string.")
        return

    # Check attendees type
    if not isinstance(attendees, list):
        print("Error: attendees must be a list of dictionaries.")
        return

    if not all(isinstance(attendee, dict) for attendee in attendees):
        print("Error: attendees must be a list of dictionaries.")
        return

    # Check empty template
    if template == "":
        print("Template is empty, no output files generated.")
        return

    # Check empty attendees list
    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    # Process attendees
    for index, attendee in enumerate(attendees, start=1):
        output = template

        placeholders = [
            "name",
            "event_title",
            "event_date",
            "event_location"
        ]

        for key in placeholders:
            value = attendee.get(key)

            if value is None:
                value = "N/A"

            output = output.replace("{" + key + "}", str(value))

        filename = f"output_{index}.txt"

        with open(filename, "w") as file:
            file.write(output)
