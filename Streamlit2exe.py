# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 13:16:10 2024

@author: danie
"""

import streamlit as st

x = st.slider("Select value:")
st.write(x,'kwadrat', x * x)