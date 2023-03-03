#!/usr/bin/env python

import sys
import click

@click.command()
@click.option('--project', '-p', required=True, default='all', show_default=True,
        help="Isabl project title")
@click.option('--application', '-a', required=True, 
        help="Isabl application name")
@click.option('--result_types', '-r', multiple=True,
        help="pandas filter applied to result_type column. If empty, no filter applied")
@click.option('--most_recent', '-mr', required=True, default=True, show_default=True,
        help="get most recent files from Isabl")
@click.option('--delimitor', '-d', required=True, default='\t', show_default=True,
        help="output file column delimitor")
def get_paths(project, application, result_types, most_recent, delimitor):
    import shahlabdata.isabl
    print("[LOG] shahlabdata.isabl module loaded", file=sys.stderr)

    query = { 
        'application': application,
        'most_recent': most_recent,
    }
    if project != 'all':
        query['project_title'] = project

    print(f"[LOG] query = {query}", file=sys.stderr)

    paths = shahlabdata.isabl.get_results(**query)
    if len(result_types) > 0:
        paths = paths[paths.result_type.isin(result_types)]
    paths.to_csv(sys.stdout, sep=delimitor, index=False)

if __name__ == '__main__':
    get_paths()
