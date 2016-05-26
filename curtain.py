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
        # print h, w
        # print height, width
        # if w <= width :
        #     new_w = w
        #     method = cv.CV_INTER_AREA
        # else :
        #     new_w = w
        #     method = cv.CV_INTER_CUBIC
        # new_h = height*w/width
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
        #print hr, wr
        #print roir.shape[0], roir.shape[1]
        # offset_h = offset_h +hr
        # if h-offset_h <= hr :
        #     #h = h-offset_h
        #     roi = roir[0:hr, 0:wr]
        #     roir = roi
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
                #print delt
                # cv2.imshow("test",crop)
                # cv2.waitKey(0)
                y_offset = offset_h #abs(delt)
                img2[y_offset:y_offset + crop.shape[0], x_offset:x_offset + crop.shape[1]] =crop
                offset_h = offset_h+abs(delt)
                # cv2.imshow("test",img2)
                # cv2.waitKey(0)
            # else :
            #     img2[y_offset:y_offset + roir.shape[0], x_offset:x_offset + roir.shape[1]] = roir
            #     offset_h = offset_h +hr
        return img2

    def croprec(self, rect):
        height, width, depth = self.img.shape
        h, w = rect
        img2 = np.zeros((h, w, depth), np.uint8)
        img2[0:h, 0:w, :3] = [255, 255, 255]
        roir =  self.img
        crop = roir[0:h, 0:w ]
        img2[0:crop.shape[0], 0:crop.shape[1]] =crop
        # cv2.imshow("test",img2)
        # cv2.waitKey(0)
        return img2

    def mosaicrec(self, rect):
        height, width, depth = self.img.shape
        cv2.imshow("test1",self.img)
        h, w = rect
        offset_h = 0
        offset_w = 0
        img2 = np.zeros((h, w, depth), np.uint8)
        img2[0:h, 0:w, :3] = [255, 255, 255]
        roir =  self.img
        iw = w/width
        jh = h/height
        print iw
        print jh
        #while ((offset_h+height) < h) :
        while ((offset_w+width) <= w):#for i in range(1,iw):
            while ((offset_h+height) <= h): #for j in range(1,jh):
                x_offset = offset_w
                y_offset = offset_h
                img2[y_offset:y_offset + roir.shape[0], x_offset:x_offset + roir.shape[1]] = roir
                offset_h = offset_h +height
            offset_w = offset_w +width
            offset_h = 0
        cv2.imshow("test1",img2)
        # cv2.waitKey(0)
        return img2

if __name__ == "__main__":
    pass
