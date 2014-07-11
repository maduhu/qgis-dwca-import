# -*- coding: utf-8 -*-
"""
/***************************************************************************
 DwCAImporter
                                 A QGIS plugin
 Import Darwin Core Archive (DwC-A) files.
                             -------------------
        begin                : 2014-07-11
        copyright            : (C) 2014 by Nicolas Noé
        email                : nicolas@niconoe.eu
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load DwCAImporter class from file DwCAImporter.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .dwca_import import DwCAImporter
    return DwCAImporter(iface)
