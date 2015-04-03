# -*- coding: utf-8 -*-
##############################################################################
#
# Author: Yannick Buron
# Copyright 2015, TODAY Clouder SASU
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License
# as published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License with
# Attribution clause along with this program. If not, see
# <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'Clouder Website',
    'version': '1.0',
    'category': 'Clouder',
    'depends': ['base','website'],
    'author': 'Yannick Buron (Clouder)',
    'license': 'Other OSI approved licence',
    'website': 'https://github.com/YannickB/clouder-website',
    'description': """
    Clouder Website
    """,
    'demo': [],
    'data': [
        'views/clouder_website_templates.xml',
    ],
    'installable': True,
    'application': True,
}