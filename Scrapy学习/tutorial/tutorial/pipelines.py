# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exporters import JsonItemExporter


# pipelines管道是用来存储数据的
# JSON导出器，导出json文件
class TutorialPipeline(object):
    def process_item(self, item, spider):

        # 1、把爬取的结果，写入文件
        file = open('spider_result.json', 'wb')

        # 2、创建导出器
        exporter = JsonItemExporter(file)

        # 3、开启导出器
        exporter.start_exporting()

        # 4、使用导出器，导出在item中配置的数据
        exporter.export_item(item)

        # 5、关闭导出器
        exporter.finish_exporting()

        # 6、关闭文件
        file.close()

        return item
