from flask import Flask, redirect, render_template, Blueprint, request, redirect
from repositories import book_repository, author_repository
from models.book import Book


# I can use bllue print or the normal @app.route, it's the same.
book_blueprint = Blueprint("books", __name__)


