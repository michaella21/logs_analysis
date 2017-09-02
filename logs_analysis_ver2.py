#!/usr/bin/env python3

import psycopg2


def get_query_results(query):
    try:
        db = psycopg2.connect(database="news")
        c = db.cursor()
        c.execute(query)
        result = c.fetchall()
        c.close()
        db.close()
        return result
    except Exception as e:
        print(e)
        exit(1)


def print_top_articles(output_file):
    """Prints the top 3 articles of all time."""
    query = """
    SELECT articles.title, count(*) AS views
    FROM log
    JOIN articles ON log.path = '/article/' || articles.slug
    GROUP BY articles.title
    ORDER BY views DESC
    LIMIT 3
    """
    # most_read_articles is a list of tuples ('title', #views) order by views
    most_read_articles = get_query_results(query)
    output_file.write(
        "(1) What are the most popular three articles of all time?\n\n")

    for article in most_read_articles:
        output_file.write('\t' + '  - "' + article[0] + '" : ' +
                          str(article[1]) + ' views\n')


def print_top_authors(output_file):
    """Prints a list of authors ranked by total article views."""
    query = """
    SELECT authors.name, count(*) AS total_views
    FROM authors
    JOIN articles ON authors.id = articles.author
    JOIN log ON log.path = '/article/' || articles.slug
    GROUP BY authors.name
    ORDER BY total_views DESC
    """
    # most_popular_author is a list of tuples ('author_name', #total_views)
    most_popular_author = get_query_results(query)
    output_file.write(
        "\n(2) Who are the most popular article authors of all time?\n\n")
    for author, views in most_popular_author:
        output_file.write('\t {} - {} total views\n'.format(author, views))


def print_errors_over_one(output_file):
    """Prints the days where more than 1% of requests were errors"""
    query = """
    SELECT subq_total.log_date, 100*(subq_error.error_ct/subq_total.total_ct)
    FROM
        (SELECT date(time) AS log_date, count(*)::real AS total_ct
        FROM log GROUP BY date(time)) AS subq_total
        JOIN
        (SELECT date(time) AS log_date, count(*) AS error_ct
        FROM log WHERE status = '404 NOT FOUND' GROUP BY date(time))
        AS subq_error ON subq_total.log_date = subq_error.log_date
    WHERE subq_error.error_ct/subq_total.total_ct > 0.01
    """
    # most_errored_date is a list of tuples ('date', % errors)
    most_errored_date = get_query_results(query)
    output_file.write(
        "\n(3) On which days did more than 1% of requests lead to errors?\n\n"
        )
    # for the error rates, round to the second decimal points
    for day in most_errored_date:
        output_file.write(
            '\t {0: %B, %d, %Y}  - {1:.2f}% errors'.format(day[0], day[1]))


if __name__ == '__main__':
    output_file = open('analysis.txt', 'w')
    print_top_articles(output_file)
    print_top_authors(output_file)
    print_errors_over_one(output_file)
