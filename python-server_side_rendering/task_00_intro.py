#!/usr/bin/python3
"""
This module generates personalized invitation files from a template
and a list of attendee dictionaries.
"""


def generate_invitations(template, attendees):
    """
    Generate invitation files from a template and a list of attendees.
    """
    # Check Input Types
    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return

    if not isinstance(attendees, list) or not all(
            isinstance(attendee, dict) for attendee in attendees):
        print("Error: Attendees must be a list of dictionaries.")
        return

    # Handle Empty Inputs
    if not template:
        print("Template is empty, no output files generated.")
        return

    if not attendees:
        print("No data provided, no output files generated.")
        return

    # Process Each Attendee
    for index, attendee in enumerate(attendees, start=1):
        output_content = template

        for placeholder in ["name", "event_title", "event_date",
                             "event_location"]:
            value = attendee.get(placeholder)
            if value is None:
                value = "N/A"
            output_content = output_content.replace(
                "{" + placeholder + "}", str(value))

        output_filename = f"output_{index}.txt"

        try:
            with open(output_filename, "w") as output_file:
                output_file.write(output_content)
        except IOError as e:
            print(f"Error writing to file {output_filename}: {e}")
