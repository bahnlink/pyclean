#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import py
import click


@click.group()
def cli():
    pass


@click.command()
def testnodb():
    py.test.cmdline.main(['-vv', '-k', 'not concretes'])


@click.command()
@click.option('--report', '-r', 'report', default='term', help='Report generation')
@click.option('--modules', '-m', 'modules', default='.', help='Modules')
def test(report, modules):
    cmd = 'py.test --cov-config .coveragerc --cov-report {report} --cov={modules} tests/'.format(
        report=report, modules=modules)
    os.system(cmd)


@click.command()
def sleep():
    cmd = 'while :; do echo "wait"; sleep 100; done'
    os.system(cmd)


cli.add_command(testnodb)
cli.add_command(test)
cli.add_command(sleep)


if __name__ == '__main__':
    cli()
