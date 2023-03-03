# p2app/engine/main.py
#
# ICS 33 Fall 2022
# Project 2: Learning to Fly
#
# An object that represents the engine of the application.
#
# This is the outermost layer of the part of the program that you'll need to build,
# which means that YOU WILL DEFINITELY NEED TO MAKE CHANGES TO THIS FILE.

import sqlite3
from p2app.events import *
import os

class Engine:
    """An object that represents the application's engine, whose main role is to
    process events sent to it by the user interface, then generate events that are
    sent back to the user interface in response, allowing the user interface to be
    unaware of any details of how the engine is implemented.
    """

    def __init__(self):
        """Initializes the engine"""
        self.connected_database = None

    def process_event(self, event):
        """A generator function that processes one event sent from the user interface,
        yielding zero or more events in response."""
        # This is a way to write a generator function that always yields zero values.
        # You'll want to remove this and replace it with your own code, once you start
        # writing your engine, but this at least allows the program to run.
        if type(event) == QuitInitiatedEvent:
            yield EndApplicationEvent()

        elif type(event) == OpenDatabaseEvent:
            if os.path.exists(event.path()) and str(event.path()).endswith(".db"):
                self.connected_database = sqlite3.connect(event.path())
                self.connected_database.execute("PRAGMA foreign_keys = ON;")
                self.connected_database.commit()
                yield DatabaseOpenedEvent(event.path())
            else:
                yield DatabaseOpenFailedEvent("database path failed")

        elif type(event) == CloseDatabaseEvent:
            yield DatabaseClosedEvent()

        elif type(event) == StartContinentSearchEvent:
            curser = None
            if event.continent_code() and event.name():
                curser = self.connected_database.execute("SELECT * FROM continent WHERE continent_code = ? AND name = ?;",(event.continent_code(),event.name()))
                self.connected_database.commit()
            if event.continent_code() is None:
                curser = self.connected_database.execute("SELECT * FROM continent WHERE name = ?;",(event.name(),))
                self.connected_database.commit()
            if event.name() is None:
                curser = self.connected_database.execute("SELECT * FROM continent WHERE continent_code = ?;",(event.continent_code(),))
                self.connected_database.commit()
            curser_namedtuple_s = curser.fetchall()
            if curser_namedtuple_s is None:
                yield None
            else:
                for curser_namedtuple in curser_namedtuple_s:
                    continent_namedtuple = Continent(curser_namedtuple[0],curser_namedtuple[1],curser_namedtuple[2])
                    yield ContinentSearchResultEvent(continent_namedtuple)

        elif type(event) == LoadContinentEvent:
            curser = self.connected_database.execute("SELECT * FROM continent WHERE continent_id = ?;",(event.continent_id(),))
            self.connected_database.commit()
            curser_namedtuple = curser.fetchone()
            continent_namedtuple = Continent(curser_namedtuple[0], curser_namedtuple[1],curser_namedtuple[2])
            yield ContinentLoadedEvent(continent_namedtuple)

        elif type(event) == SaveNewContinentEvent:
            if event.continent().continent_code == '' or event.continent().name == '':
                yield SaveContinentFailedEvent("require both a name and code for the new continent")
            else:
                try:
                    self.connected_database.execute("INSERT INTO continent (continent_code, name) VALUES (?, ?);",(event.continent().continent_code,event.continent().name))
                    self.connected_database.commit()
                    curser = self.connected_database.execute("SELECT * FROM continent WHERE continent_code = ? ;",(event.continent().continent_code,))
                    self.connected_database.commit()
                    curser_namedtuple = curser.fetchone()
                    continent_namedtuple = Continent(curser_namedtuple[0], curser_namedtuple[1],curser_namedtuple[2])
                    yield ContinentSavedEvent(continent_namedtuple)
                except sqlite3.IntegrityError:
                    yield SaveContinentFailedEvent("continent already exist")

        elif type(event) == SaveContinentEvent:
            if event.continent().continent_code == '' or event.continent().name == '':
                yield SaveContinentFailedEvent("require both a name and code for the new continent")
            else:
                try:
                    self.connected_database.execute("UPDATE continent SET continent_code = ?, name = ? WHERE continent_id = ?;",(event.continent().continent_code,event.continent().name,event.continent().continent_id))
                    self.connected_database.commit()
                    yield ContinentSavedEvent(event.continent())
                except sqlite3.IntegrityError:
                    yield SaveContinentFailedEvent("continent code already exist")

        elif type(event) == StartCountrySearchEvent:
            curser = None
            if event.country_code() and event.name():
                curser = self.connected_database.execute(
                    "SELECT * FROM country WHERE country_code = ? AND name = ?;",(event.country_code(),event.name()))
                self.connected_database.commit()
            if event.country_code() is None:
                curser = self.connected_database.execute(
                    "SELECT * FROM country WHERE name = ? ;",(event.name(),))
                self.connected_database.commit()
            if event.name() is None:
                curser = self.connected_database.execute(
                    "SELECT * FROM country WHERE country_code = ? ;",(event.country_code(),))
                self.connected_database.commit()
            curser_namedtuple_s_1 = curser.fetchall()
            if curser_namedtuple_s_1 is None:
                yield None
            else:
                for curser_namedtuple in curser_namedtuple_s_1:
                    country_namedtuple = Country(curser_namedtuple[0], curser_namedtuple[1],curser_namedtuple[2],curser_namedtuple[3],curser_namedtuple[4],curser_namedtuple[5])
                    yield CountrySearchResultEvent(country_namedtuple)

        elif type(event) == LoadCountryEvent:
            curser = self.connected_database.execute("SELECT * FROM country WHERE country_id = ?;",(event.country_id(),))
            self.connected_database.commit()
            curser_namedtuple = curser.fetchone()
            country_namedtuple = Country(curser_namedtuple[0], curser_namedtuple[1], curser_namedtuple[2], curser_namedtuple[3], curser_namedtuple[4], curser_namedtuple[5])
            yield CountryLoadedEvent(country_namedtuple)

        elif type(event) == SaveNewCountryEvent:
            if event.country().country_code == '' or event.country().name == '' or event.country().continent_id == 0 or event.country().wikipedia_link == "" or event.country().keywords == "":
                yield SaveCountryFailedEvent("missing information or continent id cannot be 0")
            else:
                try: #'country_id', 'country_code', 'name', 'continent_id', 'wikipedia_link', 'keywords'
                    self.connected_database.execute("INSERT INTO country (country_code, name, continent_id, wikipedia_link, keywords) VALUES (?, ?, ?, ?, ?);",(event.country().country_code, event.country().name, event.country().continent_id, event.country().wikipedia_link, event.country().keywords))
                    self.connected_database.commit()
                    curser = self.connected_database.execute("SELECT * FROM country WHERE country_code = ?;",(event.country().country_code,))
                    self.connected_database.commit()
                    curser_namedtuple = curser.fetchone()
                    country_namedtuple = Country(curser_namedtuple[0], curser_namedtuple[1],curser_namedtuple[2], curser_namedtuple[3], curser_namedtuple[4], curser_namedtuple[5])
                    yield CountrySavedEvent(country_namedtuple)
                except sqlite3.IntegrityError:
                    yield SaveCountryFailedEvent("country already exist")

        elif type(event) == SaveCountryEvent:
            if event.country().country_code == '' or event.country().name == '' or event.country().continent_id == 0 or event.country().wikipedia_link == "" or event.country().keywords == "":
                yield SaveCountryFailedEvent("missing information to store the country or country id cannot be 0")
            else:
                try:
                    self.connected_database.execute(
                        "UPDATE country SET country_code = ?, name = ?, continent_id = ?, wikipedia_link = ?, keywords = ? WHERE country_id = ?;",(event.country().country_code, event.country().name, event.country().continent_id, event.country().wikipedia_link, event.country().keywords, event.country().country_id))
                    self.connected_database.commit()
                    yield CountrySavedEvent(event.country())
                except sqlite3.IntegrityError:
                    yield SaveCountryFailedEvent("country code already exist")

        elif type(event) == StartRegionSearchEvent:
            curser = None
            if event.region_code() and event.local_code() and event.name():
                curser = self.connected_database.execute(
                    "SELECT * FROM region WHERE region_code = ? AND local_code = ? AND name = ?;",(event.region_code(), event.local_code(), event.name()))
                self.connected_database.commit()
            elif event.region_code() is None and event.local_code() is None:
                curser = self.connected_database.execute(
                    "SELECT * FROM region WHERE name = ?;", (event.name(),))
                self.connected_database.commit()
            elif event.region_code() is None and event.name() is None:
                curser = self.connected_database.execute(
                    "SELECT * FROM region WHERE local_code = ?;", (event.local_code(),))
                self.connected_database.commit()
            elif event.local_code() is None and event.name() is None:
                curser = self.connected_database.execute(
                    "SELECT * FROM region WHERE region_code = ?;", (event.region_code(),))
                self.connected_database.commit()
            elif event.region_code() is None:
                curser = self.connected_database.execute(
                    "SELECT * FROM region WHERE name = ? AND local_code = ?;",(event.name(),event.local_code()))
                self.connected_database.commit()
            elif event.local_code() is None:
                curser = self.connected_database.execute(
                    "SELECT * FROM region WHERE name = ? AND region_code = ?;",(event.name(),event.region_code()))
                self.connected_database.commit()
            elif event.name() is None:
                curser = self.connected_database.execute(
                    "SELECT * FROM region WHERE local_code = ? AND region_code = ?;",(event.local_code(),event.region_code()))
                self.connected_database.commit()
            curser_namedtuple_s_2 = curser.fetchall()
            if curser_namedtuple_s_2 is None:
                yield None
            else:
                for curser_namedtuple in curser_namedtuple_s_2:
                    region_namedtuple = Region(curser_namedtuple[0], curser_namedtuple[1],curser_namedtuple[2],curser_namedtuple[3],curser_namedtuple[4],curser_namedtuple[5],curser_namedtuple[6],curser_namedtuple[7])
                    yield RegionSearchResultEvent(region_namedtuple)

        elif type(event) == LoadRegionEvent:
            curser = self.connected_database.execute("SELECT * FROM region WHERE region_id = ?;",(event.region_id(),))
            self.connected_database.commit()
            curser_namedtuple = curser.fetchone()
            region_namedtuple = Region(curser_namedtuple[0], curser_namedtuple[1], curser_namedtuple[2], curser_namedtuple[3], curser_namedtuple[4], curser_namedtuple[5], curser_namedtuple[6], curser_namedtuple[7])
            yield RegionLoadedEvent(region_namedtuple)

        elif type(event) == SaveNewRegionEvent: #'region_id', 'region_code', 'local_code', 'name', 'continent_id', 'country_id', 'wikipedia_link', 'keywords'
            if event.region().region_code == '' or event.region().local_code == '' or event.region().name == '' or event.region().continent_id == 0 or event.region().country_id == 0 or event.region().wikipedia_link == '' or event.region().keywords == '':
                yield SaveRegionFailedEvent("missing information or numbers cannot be 0")
            else:
                try:
                    self.connected_database.execute("INSERT INTO region (region_code, local_code, name, continent_id, country_id, wikipedia_link, keywords) VALUES (?, ?, ?, ?, ?, ?, ?);",(event.region().region_code, event.region().local_code, event.region().name, event.region().continent_id, event.region().country_id, event.region().wikipedia_link, event.region().keywords))
                    self.connected_database.commit()
                    curser = self.connected_database.execute("SELECT * FROM region WHERE region_code = ?;",(event.region().region_code,))
                    self.connected_database.commit()
                    curser_namedtuple = curser.fetchone()
                    region_namedtuple = Region(curser_namedtuple[0], curser_namedtuple[1], curser_namedtuple[2], curser_namedtuple[3], curser_namedtuple[4], curser_namedtuple[5], curser_namedtuple[6], curser_namedtuple[7])
                    yield RegionSavedEvent(region_namedtuple)
                except sqlite3.IntegrityError:
                    yield SaveRegionFailedEvent("region code already in use. or country ID not in the continent")

        elif type(event) == SaveRegionEvent:
            if event.region().region_code == '' or event.region().local_code == '' or event.region().name == '' or event.region().continent_id == 0 or event.region().country_id == 0 or event.region().wikipedia_link == '' or event.region().keywords == '':
                yield SaveRegionFailedEvent("missing information or numbers cannot be 0")
            else:
                try:
                    self.connected_database.execute(
                        "UPDATE region SET region_code = ?, local_code = ?, name = ?, continent_id = ?, country_id = ?, wikipedia_link = ?, keywords = ? WHERE region_id = ?;",(event.region().region_code, event.region().local_code, event.region().name, event.region().continent_id, event.region().country_id, event.region().wikipedia_link, event.region().keywords, event.region().region_id))
                    self.connected_database.commit()
                    yield RegionSavedEvent(event.region())
                except sqlite3.IntegrityError:
                    yield SaveRegionFailedEvent("region code already exist or the continent id and country id can't correspond")

        else:
            yield ErrorEvent