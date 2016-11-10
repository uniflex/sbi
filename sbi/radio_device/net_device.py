from sbi.common.net_device import NetDevice

__author__ = "Piotr Gawlowicz, Anatolij Zubow"
__copyright__ = "Copyright (c) 2015, Technische Universitat Berlin"
__version__ = "0.1.0"
__email__ = "{gawlowicz, zubow}@tkn.tu-berlin.de"


class RadioNetDevice(NetDevice):
    '''
    Base Class for Radio Network Device
    '''
    def set_parameters(self, param_key_values):
        """
        The UPI_R interface is able to configure the radio and MAC behavior
        by changing parameters. Parameters correspond to the configuration
        registers of the hardware platform and to the variables used in the
        radio programs. This function (re)set the value(s) of the parameters
        specified in the dictionary argument. The list of available parameters
        supported by all platforms are defined in this module. Parameters
        specific to a subgroup of platforms are defined in the corresponding
        submodules. A list of supported parameters can be dynamically obtained
        using the get_radio_info function.

        Examples:
            .. code-block:: python

                >> param_key_values = {CSMA_CW : 15, CSMA_CW_MIN : 15,
                                       CSMA_CW_MAX : 15}
                >> result = control_engine.radio.iface("wlan0").set_parameters(param_key_values)
                >> print result
                {CSMA_CW : 0, CSMA_CW_MIN : 0, CSMA_CW_MAX : 0}

        Args:
            param_key_values (dict): dictionary containing the key (string)
                value (any) pairs for each parameter.
                An example is:
                {CSMA_CW : 15, CSMA_CW_MIN : 15, CSMA_CW_MAX : 15}

        Returns:
            dict: A dictionary containing key (string name) error
                 (0 = success, 1=fail, +1=error code) pairs for each parameter.
        """
        raise NotImplementedError

    def get_parameters(self, param_key_list):
        """
        The UPI_R interface is able to obtain the current radio and MAC
        configuration by getting parameter values. Parameters correspond
        to the configuration registers of the hardware platform and to
        the variables used in the radio programs. This function get(s)
        the value(s) of the parameters specified in the list argument.
        The list of available parameters supported by all platforms are
        defined in this module. Parameters specific to a subgroup of
        platforms are defined in the corresponding submodules. A list
        of supported parameters can be dynamically obtained using the
        get_radio_info function.

        Examples:
            .. code-block:: python

                >> param_keys = [CSMA_CW,CSMA_CWMIN]
                >> result = control_engine.radio.iface("wlan0").get_parameters(param_keys)
                >> print result
                {CSMA_CW : 15, CSMA_CWMIN : 15}

        Args:
            param_key_list (list): list of parameter names.
                An example is:
                [UPI_RN.CSMA_CW, UPI_RN.CSMA_CW_MIN, UPI_RN.CSMA_CW_MAX].

        Returns:
            dict: A dictionary containing key (string name)
                  and values of the requested parameters.
         """
        raise NotImplementedError

    def get_measurements(self, measurement_key_list):
        """
        The UPI_R interface is able to get the radio measurements
        in a pull based manner. The low-level measurements are
        continuously monitored by the hardware platform and by
        the radio programs. They can be used to get information
        and statistics about the state of the physical links or
        the internal state of the node. This function gets the
        measurements specified in the list argument and returns
        a dictionary with their values. The list of available
        measurements supported by all platforms are defined in
        this module. Measurements specific to a subgroup of
        platforms are defined in the corresponding submodules.
        A list of supported measurements can be dynamically
        obtained using the get_radio_info function.

        Examples:
            .. code-block:: python

                >> measurement_keys = [NUM_FREEZING_COUNT]
                >> result = control_engine.radio.iface("wlan0").get_measurements(measurement_keys)
                >> print result
                {UPI_RN.NUM_FREEZING_COUNT : 150}

        Args:
            measurement_key_list (list): list of requested measurements.
                An example is [NUM_FREEZING_COUNT, TX_ACTIVITY].

        Returns:
            dict: A dictionary containing key (string name)
                  and values of the requested measurements.
        """
        raise NotImplementedError

    # Activation and deactivation of radio programs.

    def activate_radio_program(self, name):
        """
        This function activates the specified radio program.
        When executed, this function stops the current radio
        program and enables the execution of the radio program
        specified in the parameter name.

        Examples:
            .. code-block:: python

               >> result = control_engine.radio.iface("wlan0").activate_radio_program("CSMA")
               >> print result
               0

        Args:
            name (str): String identifier of the radio program,
                        (e.g. CSMA, TDMA, TSCH)

        Returns:
            int: - 0 if the parameter setting call was successfully performed
                - 1 partial success
                - 2 error.
        """
        raise NotImplementedError

    def deactivate_radio_program(self, name):
        """
        When executed, this function stops the radio program
        specified in the parameter radio_program_name.

        Examples:
            .. code-block:: python

                >> result = control_engine.radio.iface("wlan0").deactivate_radio_program("CSMA")
                >> print result
                0

        Args:
            name (str): String identifier of the radio program
                        (e.g. CSMA, TDMA, TSCH)

        Returns:
            int:
                - 0 if the parameter setting call was successfully performed
                - 1 partial success
                - 2 error.
        """
        raise NotImplementedError

    def get_running_radio_program(self):
        """
        Returns active radio program.

        Each radio program is associated with a name and an index.
        When executed, this function return the index of the
        radio program active.

        Examples:
            .. code-block:: python

                >> args = {'interface' : 'wlan0'}
                >> result = control_engine.radio.iface("wlan0").getActive(args)
                >> print result
                CSMA

        Args:
            myargs:
                a dictionary data type (key: value) where the keys are:
                The key "interface" specify the network interface to use.

        Returns:
            the name of the active radio program
        """
        raise NotImplementedError

    def get_radio_platforms(self):
        """
        Gets available radio platforms. The information elements used
        by the UPI_R interface, to manage parameters, measurements
        and radio program, are organized into data structures, which
        provide information on the platform type and radio capabilities.
        When executed, this function return information about available
        interfaces on node, the name or the identifier of the interface
        and the supported platform type.

        Example:
            .. code-block:: python

                >> radio_platform_list = radio_platform_t()\n
                >> nic_list = control_engine.radio.iface("wlan0").get_radio_platforms()
                >> nic_list.platform_info =  nic_list[0]
                >> nic_list.platform =  nic_list[1]

        Args:

        Returns:
            current_NIC_list:
                a list of pair value, the first value is the interface
                identifier and the second is the supported platforms.
        """
        raise NotImplementedError

    def get_radio_info(self, platform_id):
        """
        Gets the radio capabilities of a given network card radio_platform_t
        in terms of supported measurement and supported parameter and list
        of supported radio program. The information elements used by the
        UPI_R interface, to manage parameters, measurements and radio program,
        are organized into data structures, which provide information
        on the platform type and radio capabilities. When executed, this
        function return information about available radio capabilities
        (measurements and parameters) of each interface (radio_platform_t)
        on the available radio programs (radio_prg_t) available for
        transmissions over the radio interface.

        Example:
            .. code-block:: python

                >> platform_info = radio_info_t()
                >> platform_info_str = control_engine.radio.iface("wlan0").getRadioInfo(platform_id)
                >> platform_info.platform_info.platform_id = current_platform_info_str['radio_info'][0]
                >> platform_info.platform_info.platform = current_platform_info_str['radio_info'][1]
                >> platform_info.monitor_list = current_platform_info_str['monitor_list']
                >> platform_info.param_list = current_platform_info_str['param_list']
                >> platform_info.execution_engine_list_name = current_platform_info_str['exec_engine_list_name']
                >> platform_info.execution_engine_list_pointer = current_platform_info_str['exec_engine_list_pointer']
                >> platform_info.radio_program_list_name = current_platform_info_str['radio_prg_list_name']
                >> platform_info.radio_program_list_path = current_platform_info_str['radio_prg_list_pointer']

        Args:
         interface:
            network interfaces to use

        :Returns
            result:
                return a list in term of a dictionary data type,
                in which are present the key showed below:
                'radio_info' --> a list of pair value, the first value is the
                                 interface identifier and the second is the
                                 supported platforms
                'monitor_list' --> a list of supported measurements between
                                   the attribute of the class UPI_R
                'param_list' --> a list of supported Parameters between the
                                 attribute of the class UPI_R
                'exec_engine_list_name' --> a list of supported
                                            execution_engine_list_pointer
                                            environment name
                'exec_engine_list_pointer' --> a list of supported execution
                                               environment path
                'radio_prg_list_name'--> a list of supported radio program name
                'radio_prg_list_pointer' --> a list of supported radio
                                             program path
        """
        raise NotImplementedError

    ''' Transmission of radio waveform (no MAC) '''

    def play_waveform(self, iface, freq, power_lvl, **kwargs):
        '''
        Starts transmitting a radio waveform (just PHY, no MAC).
        '''
        raise NotImplementedError

    def stop_waveform(self, iface, **kwargs):
        '''
        Stops transmitting a radio waveform.
        '''
        raise NotImplementedError

    def set_tx_power(self, power_dBm, iface):
        '''
        Set transmission power for a give interface
        '''
        raise NotImplementedError

    def get_tx_power(self, iface):
        '''
        Get transmission power of given interface
        '''
        raise NotImplementedError

    def get_noise(self):
        '''
        Returns the noise floor measured by the wireless driver.
        '''
        raise NotImplementedError

    def get_interfaces(self):
        '''
        Returns all network interfaces of device
        '''
        raise NotImplementedError

    def get_interface_info(self, ifaceName):
        '''
        Returns info on network interface
        '''
        raise NotImplementedError

    def get_phy_info(self, ifaceName):
        '''
        Returns info of phy
        '''
        raise NotImplementedError

    def add_interface(self, ifaceName, mode):
        '''
        Add wireless interface with ifaceName and mode
        '''
        raise NotImplementedError

    def del_interface(self, ifaceName):
        '''
        Delete interface by name
        '''
        raise NotImplementedError

    def set_interface_up(self, ifaceName):
        '''
        Set interface UP
        '''
        raise NotImplementedError

    def set_interface_down(self, ifaceName):
        '''
        Set interface DOWN
        '''
        raise NotImplementedError

    def is_interface_up(self, ifaceName):
        '''
        Check if interface is up
        '''
        raise NotImplementedError

    def get_link_info(self, interfaceName):
        '''
        Get link info of interface
        '''
        raise NotImplementedError

    def is_connected(self, interfaceName):
        '''
        Check if interface is in connected state
        '''
        raise NotImplementedError

    def disconnect(self, interfaceName):
        '''
        Disconnect interface
        '''
        raise NotImplementedError

    def get_regulatory_domain(self):
        '''
        Returns the regulatory domain (for all interfaces)
        '''
        raise NotImplementedError

    def set_regulatory_domain(self, new_domain):
        '''
        Sets the regulatory domain (for all interfaces)
        '''
        raise NotImplementedError
