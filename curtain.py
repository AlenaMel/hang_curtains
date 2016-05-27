#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, cv2
import cv2.cv as cv
import numpy as np


class Curtain:
    def __init__(self, fname):
        self.img = cv2.imread(fname)


    def resize_w(self, rect, met):
        height, width, depth = self.img.shape
        h, w = rect
        rimg = cv2.resize(self.img,(int(w),int(h)), met)
        # cv2.imshow("test",rimg)
        # cv2.waitKey(0)
        return rimg

    def fillrec(self, rect):
        height, width, depth = self.img.shape
        h, w = rect
        offset_h = 0
        if w <= width :
            wr = w
            method = cv.CV_INTER_AREA
        else :
            wr = w
            method = cv.CV_INTER_CUBIC
        hr = height*w/width
        roir = self.resize_w((hr, wr),method)
        hr,wr,dd = roir.shape
        img2 = np.zeros((h, w, depth), np.uint8)
        img2[0:h, 0:w, :3] = [255, 255, 255]
        while ((offset_h+hr) < h) :
            x_offset = 0
            y_offset = offset_h
            img2[y_offset:y_offset + roir.shape[0], x_offset:x_offset + roir.shape[1]] = roir
            offset_h = offset_h +hr
            delt = h-(offset_h+hr)
            if (delt < 0) :
                crop = roir[0:delt, 0:w ]
                print delt
                # cv2.imshow("test",crop)
                # cv2.waitKey(0)
                y_offset = offset_h
                img2[y_offset:y_offset + crop.shape[0], x_offset:x_offset + crop.shape[1]] =crop
                offset_h = offset_h+abs(delt)
        return img2

    def croprec(self, rect):
        height, width, depth = self.img.shape
        h, w = rect
        img2 = np.zeros((h, w, depth), np.uint8)
        img2[0:h, 0:w, :3] = [255, 255, 255]
        roir = self.img
        crop = roir[0:h, 0:w]
        img2[0:crop.shape[0], 0:crop.shape[1]] = crop
        # cv2.imshow("test",img2)
        # cv2.waitKey(0)
        return img2

    def mosaicrec(self, rect):
        height, width, depth = self.img.shape
        cv2.imshow("test1", self.img)
        h, w = rect
        offset_h = 0
        offset_w = 0
        img2 = np.zeros((h, w, depth), np.uint8)
        img2[0:h, 0:w, :3] = [255, 255, 255]
        roir = self.img
        deltw = width
        delt = height
        while ((offset_w+abs(deltw)) <= w):
            while ((offset_h + height) <= h):
                x_offset = offset_w
                y_offset = offset_h
                img2[y_offset:y_offset + roir.shape[0], x_offset:x_offset + roir.shape[1]] = roir
                offset_h = offset_h + height
                delt = h - (offset_h + height)
                if (delt < 0):
                    crop = roir[0:delt, 0:w]
                    y_offset = offset_h
                    img2[y_offset:y_offset + crop.shape[0], x_offset:x_offset + crop.shape[1]] = crop
                else:
                    delt = height
            offset_w = offset_w + width
            offset_h = 0
            deltw = w - (offset_w + width)
            # print "deltw", deltw
            # print "offset_w", offset_w
            if (deltw < 0):
                cropw = roir[0:h, 0:deltw]
                x_offset = offset_w
                y_offset = 0
                img2[y_offset:y_offset + cropw.shape[0], x_offset:x_offset + cropw.shape[1]] = cropw
                while ((offset_h + height) <= h):
                    x_offset = offset_w
                    y_offset = offset_h
                    img2[y_offset:y_offset + cropw.shape[0], x_offset:x_offset + cropw.shape[1]] = cropw
                    offset_h = offset_h + height
                    delt = h - (offset_h + height)
                    if (delt < 0):
                        crop = cropw[0:delt, 0:w]
                        y_offset = offset_h
                        img2[y_offset:y_offset + crop.shape[0], x_offset:x_offset + crop.shape[1]] = crop
                    else:
                        delt = height
            else:
                deltw = width
        cv2.imshow("test1", img2)
        # cv2.waitKey(0)
        return img2


if __name__ == "__main__":
    pass
